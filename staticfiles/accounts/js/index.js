let nav = document.querySelector('nav');

window.addEventListener('scroll', function(event) 
{
    event.preventDefault();

    if (window.scrollY >=600) 
    {
        nav.style.backgroundColor = 'rgba(28,74,90, 1)';
    }
    else
    {
        nav.style.backgroundColor = 'transparent';
    }
});