document.addEventListener("DOMContentLoaded", function() {
    // New tab when opening external link in navigation menu
    document.querySelectorAll('.site-nav a[href^="http"]').forEach(link => {
        if (!link.href.includes(window.location.origin)) {
            link.setAttribute("target", "_blank");
            link.setAttribute("rel", "noopener noreferrer");
        }
    });
});
