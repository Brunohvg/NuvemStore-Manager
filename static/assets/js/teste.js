// Primeiro, selecione todos os itens do menu
var itensMenu = document.querySelectorAll('.nav-item');

// Em seguida, percorra cada item do menu
itensMenu.forEach(item => {
    // Obtenha o link dentro do item do menu
    var link = item.querySelector('.nav-link');

    // Verifique se o href do link corresponde à URL atual
    if (link.getAttribute('href') === window.location.pathname) {
        // Se corresponder, adicione a classe 'active' ao item do menu
        link.classList.add('active');
    } else {
        // Se não corresponder, remova a classe 'active' (se existir)
        link.classList.remove('active');
    }
});


// Selecione e ative os itens do submenu
var subMenuItens = document.querySelectorAll('.nav-link.submenu-toggle');

subMenuItens.forEach(subMenuItem => {
    // Verifique se o link atual possui a classe 'active'
    if (subMenuItem.getAttribute('href') === window.location.pathname) {
        // Adicione a classe 'active' ao link atual
        subMenuItem.classList.add('active');

        // Encontre o elemento .collapse dentro deste item do submenu
        var subMenuCollapse = subMenuItem.nextElementSibling;
        if (subMenuCollapse.classList.contains('collapse')) {
            subMenuCollapse.classList.add('show');
        }
    }
});

document.addEventListener('DOMContentLoaded', function () {
    var currentURL = window.location.pathname;

    var subMenuLinks = document.querySelectorAll('.submenu-link');

    subMenuLinks.forEach(function (link) {
        if (link.getAttribute('href') === currentURL) {
            link.classList.add('active');
        }
    });
});
