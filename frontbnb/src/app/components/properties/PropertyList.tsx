'use client';

import { useEffect, useState } from "react";

import PropertyListItem from "./PropertyListItem";

export type PropertyListType = {
    id: string;
    title: string;
    price_per_night: number;
    image_url: string;
}

const PropertyList = () => {
    const [properties, setProperties] = useState<PropertyListType[]>([]);

    const getProperties = async () => {
        const url = 'http://localhost:8000/api/properties/';
        
        await fetch(url, {
            method: 'GET',
        },
        ).then(response => response.json())
        .then((data) => {
            console.log("Données récupérées:", data);

            setProperties(data.data);

        })
        .catch((error) => console.error("Erreur lors de la récupération :", error));
    };

    useEffect(() => {
        getProperties();
    },[]);

    return( 
        <>
            {properties.map((property) => (
                <PropertyListItem  
                    key={property.id}
                    property={property}
                />
            ))}
        </>
    )
}
export default PropertyList;