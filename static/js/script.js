// Alterna o modo noturno
const themeToggleButton = document.getElementById('theme-toggle');
const body = document.body;

// O modo noturno estará sempre ativado sem necessidade de alternância
document.body.classList.add('dark-mode');


themeToggleButton.addEventListener('click', () => {
    // Alterna entre os modos
    body.classList.toggle('dark-mode');
    
    // Salva a preferência do usuário no localStorage
    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('dark-mode', 'enabled');
    } else {
        localStorage.setItem('dark-mode', 'disabled');
    }
});
