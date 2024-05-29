// Add a tile layer to the map using OpenStreetMap
let street = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

// Create an empty array to hold the coordinates
let mappoints = [];



// Use D3 to load the GeoJSON data
d3.json("../../data/geojson_coordinates.json").then(function(data) {
    data.features.forEach(function(feature) {
        mappoints.push(L.Markers(
            feature.geometry.coordinates));
    })
});

let mappointsLayer = L.layerGroup(mappoints);

let overlayMaps = {
    "All Care Homes": mappointsLayer
};

// Create a map using Leaflet
let myMap = L.map("map", {
    center: [52.5022, -2.1184],
    zoom: 12,
    layers: [street, mappointsLayer]
});


L.control.layers(null, overlayMaps).addTo(myMap);