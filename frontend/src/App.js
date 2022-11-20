import './App.css';
import { MapContainer, TileLayer } from 'react-leaflet'
// import L from "leaflet";
import React from 'react';
import UserTracker from './UserTracker';

function App() {
  return (
    <MapContainer center={[48.1351, 11.5820]} zoom={15} zoomControl={false} >
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <UserTracker />
    </MapContainer>
  );
}

export default App;
