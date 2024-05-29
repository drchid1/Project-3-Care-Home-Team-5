// Add a tile layer to the map using OpenStreetMap
let street = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

// Create a map using Leaflet
let myMap = L.map("map", {
    center: [52.5022, -2.1184],
    zoom: 12,
    layers: [street]
});

// Create an empty array to hold the coordinates
let mappoints = [];
let nhMarkers = [];
let ldMarkers = [];
let dMarkers = [];
let pdMarkers = [];
let yaMarkers = [];
let siMarkers = [];
let mMarkers = [];

// Use D3 to load the GeoJSON data
d3.json("../../data/geojson_coordinates.json").then(function(data) {
    data.features.forEach(function(feature) {
        let marker = L.marker(feature.geometry.coordinates).bindPopup(`<h3>${feature.properties.formattedAddress.split(',')[0]}</h3> <hr> <h5>Email: ${feature.properties.email}</h5> <h5>Telephone: ${feature.properties.telephoneNo}</h5> <h5>Features: ${feature.properties.cqcRegisteredFor}</h5>`);
        mappoints.push(marker);
        // marker.addTo(myMap);

        // create a list of markers if feature.properties.provideNursing === "Yes"
        if (feature.properties.provideNursing === "Yes") {
            nhMarkers.push(marker);
        };
        if (feature.properties.cqcRegisteredFor) {
            let type = feature.properties.cqcRegisteredFor.toString();
            if (type.includes("Learning Disability")) {
                ldMarkers.push(marker);
            };
        };
        if (feature.properties.cqcRegisteredFor) {
            let type = feature.properties.cqcRegisteredFor.toString();
            if (type.includes("Dementia")) {
                dMarkers.push(marker);
            };
        };
        if (feature.properties.cqcRegisteredFor) {
            let type = feature.properties.cqcRegisteredFor.toString();
            if (type.includes("Physical Disability")) {
                pdMarkers.push(marker);
            };
        };
        if (feature.properties.cqcRegisteredFor) {
            let type = feature.properties.cqcRegisteredFor.toString();
            if (type.includes("Younger Adults")) {
                yaMarkers.push(marker);
            };
        };
        if (feature.properties.cqcRegisteredFor) {
            let type = feature.properties.cqcRegisteredFor.toString();
            if (type.includes("Sensory Impairment")) {
                siMarkers.push(marker);
            };
        };
        if (feature.properties.cqcRegisteredFor) {
            let type = feature.properties.cqcRegisteredFor.toString();
            if (type.includes("Mental")) {
                mMarkers.push(marker);
            };
        };


    });

    // let mappointsLayer = L.layerGroup(mappoints);
    // let nhLayer = L.layerGroup(nhMarkers);

    let overlayMaps = {
        "All Care Homes": L.layerGroup(mappoints),
        "Provides Nursing Care": L.layerGroup(nhMarkers),
        "Provides Learning Disability Care": L.layerGroup(ldMarkers),
        "Provides Dementia Care": L.layerGroup(dMarkers),
        "Provides Physical Disability Care": L.layerGroup(pdMarkers),
        "Provides Younger Adults Care": L.layerGroup(yaMarkers),
        "Provides Sensory Impairment Care": L.layerGroup(siMarkers),
        "Provides Mental Health Care": L.layerGroup(mMarkers)
    };

    L.control.layers(null, overlayMaps).addTo(myMap);
});