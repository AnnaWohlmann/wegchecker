import './App.css';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import L from "leaflet";
import React from 'react';
import UserTracker from './UserTracker';

const mockIssues = [
  [173529288004582, 11.61430161647961, 48.111355593621, 154359841, "footway"],
  [187098909929555, 11.606248275586244, 48.17566584451249, 38690109, "footway"],
  [216283226982432, 11.63329945842623, 48.13569262741428, 460354029, "footway"],
  [269290068323331, 11.58813361092573, 48.1765304782419, 259583217, "footway"],
  [305399287917735, 11.570784175202212, 48.14912076050485, 122159109, "primary"],
  [308707770748550, 11.60678544203654, 48.17607553069282, 38690109, "primary"],
  [310698823750341, 11.5806306, 48.106241100000005, 362796882, "footway"],
  [315970676772352, 11.613351477617488, 48.13046701048668, 122002285, "footway"],
  [334213504878448, 11.622674470519335, 48.16163430223077, 38926857, "primary"],
  [387616345626796, 11.608645678780396, 48.172420882348, 99663070, "primary"],
  [432081875138552, 11.547805204701106, 48.11291668736461, 173096616, "footway"],
  [486527229463839, 11.6237920164228, 48.16265466072837, 100945239, "footway"],
  [497792407930066, 11.61900312193212, 48.118031503459626, 49915865, "footway"],
  [507005454009469, 11.60673962645799, 48.17604819685549, 38690109, "primary"],
  [518223702859508, 11.62046123985182, 48.12177302648248, 292781203, "primary"],
  [532051091386866, 11.615932367309346, 48.11290549141834, 32256065, "primary"],
  [568493717757567, 11.61818097587384, 48.11925483880852, 27334574, "footway"],
  [677806630089122, 11.616833182061308, 48.16881681797188, 38123963, "primary"],
  [742794133052728, 11.5873091, 48.104692400000005, 40108148, "primary"],
  [796584247628919, 11.603695515414293, 48.17208671297508, 38690109, "footway"],
  [811604529752448, 11.615292419261202, 48.11211300211448, 37666015, "primary"],
  [821061125222211, 11.525206316022905, 48.14868644684231, 54200279, "primary"],
  [824423578448957, 11.601411486290576, 48.171796512604, 159686837, "primary"],
  [827676088105008, 11.549527023953246, 48.16089514763812, 90165750, "footway"],
  [877953149735095, 11.618987385257748, 48.11835266871433, 230251455, "primary"],
  [927816371125415, 11.624135105357796, 48.16302274431093, 467655365, "footway"],
  [952367918873603, 11.541217267708962, 48.10089803370931, 262486709, "footway"],
  [1998769373606723, 11.617648147817643, 48.11503273780353, 311181487, "footway"],
  [2096254440714769, 11.613106928911195, 48.17299008497127, 37208105, "primary"],
  [2947015848899610, 11.527965543942017, 48.14774795111176, 54200280, "footway"]
];

const OSM_marker_icon = L.icon({
  iconSize: [25, 30],

  iconUrl: require('./assets/OSM_marker.png')
});

function App() {
  return (
    <MapContainer center={[48.1351, 11.5820]} zoom={15} zoomControl={false} >
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <UserTracker />
      {
        mockIssues.map((mockIssue) => {
          return (
            <Marker position={[mockIssue[2], mockIssue[1]]} key={mockIssue[0]} icon={OSM_marker_icon}>
              <Popup style={{ maxWidth: "70vw", maxHeight: "90vh" }}>
                Way ID: {mockIssue[3]} <br /> Classification: {mockIssue[4]} <br /> <img style={{ maxWidth: "70vw", maxHeight: "90vh" }} alt={`OEM Issue for way ${mockIssue[3]}`} src={require(`./assets/mock_data/issues/${mockIssue[0]}.jpg`)} />
              </Popup>
            </Marker>
          );
        })
      }
    </MapContainer>
  );
}

export default App;