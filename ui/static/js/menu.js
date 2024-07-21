document.addEventListener('alpine:init', () => {
    Alpine.store('menu').setActive('menu');
    Alpine.store('categories', {
        data: [],
        setData: function(data) {
            this.data = data;
        }
    })
    Alpine.store('menus', {
        data: [],
        filters: {
            category: '',
        },
        setData: function(data) {
            this.data = data;
        }
    })
    Alpine.store('data', {
        menu: {},
        setMenu: function(menu) {
            this.menu = menu;
        }
    })
    
    fetchCategories();
    fetchMenu();
})

function fetchCategories() {
    fetch("/menu/categories", {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        Alpine.store('categories').setData(data);
    })
}

function fetchMenu(category) {
    let url = "/menu/read";

    if (category) {
        url += `?category=${category}`;
    }
    
    fetch(url, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        Alpine.store('menus').setData(data);
    })
}

function saveMenu() {
    data = Alpine.store('data').menu;

    let url = '/menu/save';

    let headers = {
        'Content-Type': `application/json`,
        'X-CSRFToken': getCsrfToken(),
    }

    fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    })
    .then(response => {
        return response.json().then(data => ({ status: response.status, data }));
    })
    .then(response => {
        if (response.status === 200) {
            Swal.fire({
              icon: "success",
              title: "Notification",
              text: "Successfully saved!",
            });
            document.getElementById('close-menu-modal').click();
            fetchMenu();
            Alpine.store('data').setMenu({});
        } else if (response.status === 400) {
            Swal.fire({
              icon: "error",
              title: "Notification",
              text: response.data.message,
            });
        } else {
            Swal.fire({
              icon: "error",
              title: "Notification",
              text: "Unable to save data. Please contact the administrator!",
            });
        }
    })
}

function editMenu(menu) {
    Alpine.store('data').setMenu({...menu});
    document.getElementById('create-modal-trigger').click();
}

function deleteMenu(menu) {
    Swal.fire({
      title: `Are you sure you want to delete this menu: ${menu.name}?`,
      showCancelButton: true,
      confirmButtonText: "Yes",
      denyButtonText: `Cancel`
    }).then((result) => {
      if (result.isConfirmed) {
          let url = '/menu/delete';

          let headers = {
              'Content-Type': `application/json`,
              'X-CSRFToken': getCsrfToken(),
          }

          fetch(url, {
              method: 'POST',
              headers: headers,
              body: JSON.stringify(menu)
          })
          .then(response => {
              return response.json().then(data => ({ status: response.status, data }));
          })
          .then(response => {
              if (response.status === 200) {
                  Swal.fire({
                    icon: "success",
                    title: "Notification",
                    text: "Successfully deleted!",
                  });
                  fetchMenu();
              } else if (response.status === 400) {
                  Swal.fire({
                    icon: "error",
                    title: "Notification",
                    text: response.data.message,
                  });
              } else {
                  Swal.fire({
                    icon: "error",
                    title: "Notification",
                    text: "Unable to save data. Please contact the administrator!",
                  });
              }
          })
      }
    });
}