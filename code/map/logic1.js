let nhMarkers = [];

// Use D3 to load the GeoJSON data
d3.json("../../data/geojson_coordinates.json").then(function(data) {
    // Create an empty array to hold the coordinates
    // let chData = [];
    // let pnMarkers = [];
    
  
    /* Loop through the data to get the coordinates
    and save them in the eqPoints array */
    data.features.forEach(function(feature) {
       /* if (feature.properties.provideNursing === "Yes") {
            pnMarkers.push(L.marker([
                feature.geometry.coordinates[0],
                feature.geometry.coordinates[1]]).bindPopup(`<h3>${feature.properties.formattedAddress.split(',')[0]}</h3> <hr> <h5>Email: ${feature.properties.email}</h5> <h5>Telephone: ${feature.properties.telephoneNo}</h5>`)
            );
        } */
    //     chData.push([
    //       feature.geometry.coordinates[0],
    //       feature.geometry.coordinates[1],
    //       feature.properties.formattedAddress.split(',')[0],
    //       feature.properties.formattedAddress,
    //       feature.properties.email,
    //       feature.properties.telephoneNo
    //   ]);
        console.log(feature.geometry.coordinates);
        nhMarkers.push(L.marker(
            feature.geometry.coordinates) /*.bindPopup(`<h3>${feature.properties.formattedAddress.split(',')[0]}</h3> <hr> <h5>Email: ${feature.properties.email}</h5> <h5>Telephone: ${feature.properties.telephoneNo}</h5>`)*/
        
        );
    });
});

let nhLayer = L.layerGroup(nhMarkers);

// Add a tile layer to the map using OpenStreetMap
let street = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});


let baseMaps = {
    Street: street
  };

// Create a layer
// let pnLayer = L.layerGroup(pnMarkers);

// Toggle the layer on and off
let overlayMaps = {
    "All Care Homes": nhLayer,
    // "Provides Nursing Care": pnLayer
};

// Create a map using Leaflet
let myMap = L.map("map", {
    center: [52.5022, -2.1184],
    zoom: 12,
    layers: [street, nhLayer]
});



// Create a red marker for the hospital
L.marker([52.5022,-2.1184], {
    draggable: true,
    title: "Care Homes",
    icon: L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
    })
}).bindPopup(`<h3>Russellss Hall Hospital</h3> <hr> <h5>Telephone: 01384 456111</h5>
    <h5>Address: Pensnett Rd, Dudley DY1 2HQ</h5>`).addTo(myMap);






// Layer control for the map
L.control.layers(baseMaps, overlayMaps).addTo(myMap);

/* Loop through the coordinates array and add a marker for each
coordinate and bind a popup with the title, place and time */
// chData.forEach(function(info) {
//     let [lat, lon, cHomeName, cHomeAdd, email, tel ] = info;
//     L.marker([lat,lon], {
//     draggable: true,
//     title: "Care Home"
//     }).bindPopup(`<h3>${cHomeName}</h3> <hr> <h5>Email: ${email}</h5> <h5>Telephone: ${tel}</h5>
//     <h5>Address: ${cHomeAdd}</h5>`).addTo(myMap);
// });
  
  
//   // Position the legend in the bottom right corner
//   let legend = L.control({position: 'bottomright'});
  
//   // Creating the div element for the legend
//   legend.onAdd = function () {
//     let div = L.DomUtil.create('div', 'info legend'),
//     legLabels = [-10,10, 30, 50, 70, 90],  // Labels for the legend
//     legColours = ['#83ed26', '#bbed26', '#ede026', '#edb126', '#ed9426',
//                   '#ed3d26']; // Colours for the legend
  
//     // Loop through the labels and generate a coloured square for each label
//     for (let i = 0; i < legLabels.length; i++) {
//         div.innerHTML +=
//           `<i class="square" style="background:${legColours[i]}"></i> ${legLabels[i]}${legLabels[i + 1] ? '&ndash;' + legLabels[i + 1] + '<br>' : '+'}`;
//     }
//       return div;
//   };
  
//   // Add the legend to the map
//   legend.addTo(myMap);
  

  