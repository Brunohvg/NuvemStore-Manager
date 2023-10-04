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
var subMenuItens = document.querySelectorAll('.submenu-toggle');

// Percorra cada item do submenu
subMenuItens.forEach(subMenuItem => {
    // Obtenha o link dentro do item do submenu
    var subMenuLink = subMenuItem.querySelector('.nav-link');

    // Verifique se o href do link corresponde à URL atual
    if (subMenuLink.getAttribute('href') === window.location.pathname) {
        // Se corresponder, adicione a classe 'active' ao item do submenu pai
        subMenuItem.classList.add('active');
    } else {
        // Se não corresponder, remova a classe 'active' (se existir)
        subMenuItem.classList.remove('active');
    }
});
