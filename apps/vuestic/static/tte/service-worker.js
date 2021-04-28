importScripts("/vuestic/static/tte/precache-manifest.99c0007c6b238f0ebca862920c251b12.js", "/vuestic/static/tte/workbox-v4.3.1/workbox-sw.js");
workbox.setConfig({
    modulePathPrefix: "/workbox-v4.3.1"
});
self.__precacheManifest = [].concat(self.__precacheManifest || [])
workbox.precaching.suppressWarnings()
workbox.precaching.precacheAndRoute(self.__precacheManifest, {})

workbox.routing.registerRoute(
    /\.(?:png|gif|jpg|jpeg|svg)$/,
    workbox.strategies.staleWhileRevalidate(0),
)

workbox.routing.registerRoute(
    new RegExp('https://reqres.in'),
    workbox.strategies.networkFirst(),
)