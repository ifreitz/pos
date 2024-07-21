document.addEventListener('alpine:init', () => {
    Alpine.store('menu', {
        active: 'dashboard',
        setActive: function(menu) {
            this.active = menu;
        }
    });
})

function getCsrfToken() {
    return document.getElementsByName('csrfmiddlewaretoken')[0].value;
}