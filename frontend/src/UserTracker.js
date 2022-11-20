import avi from './deer-removebg-preview.png';
import L from "leaflet";
import { useMap } from 'react-leaflet'
import React, { useState, useEffect } from 'react';
import { LeafletTrackingMarker } from "react-leaflet-tracking-marker";

const icon = L.icon({
    iconSize: [60, 50],
    popupAnchor: [2, -20],
    iconUrl: avi
});

const UserTracker = () => {
    const [pos, setPos] = useState();
    const map = useMap();

    useEffect(() => {
        map.locate().on("locationfound", function (e) {
            setPos(e.latlng);
            map.setView(e.latlng, map.getZoom())
        });
    }, []);

    useEffect(() => {
        map.locate().on("locationfound", function (e) {
            setPos(e.latlng);
        });
    }, [map]);

    const { lat, lng } = pos ? pos : { lat: 40.505, lng: -100.09 };
    const [prevPos, setPrevPos] = useState([lat, lng]);

    useEffect(() => {
        if (prevPos[1] !== lng && prevPos[0] !== lat) setPrevPos([lat, lng]);
    }, [lat, lng, prevPos]);

    return (
        <LeafletTrackingMarker
            icon={icon}
            position={[lat, lng]}
            previousPosition={prevPos}
            duration={1000}
        />
    )
}

export default UserTracker