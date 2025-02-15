document.addEventListener("DOMContentLoaded", function() {
    // New tab when opening external link in navigation menu
    document.querySelectorAll('.site-nav a').forEach(link => {
        if (link.hostname && link.hostname !== window.location.hostname) {
            link.setAttribute("target", "_blank");
            link.setAttribute("rel", "noopener noreferrer");
        }
    });
});
