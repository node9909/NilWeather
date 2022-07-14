<script setup>

import './assets/styles/app.scss';

import { ref } from '@vue/reactivity';
import { watch } from '@vue/runtime-core';
import axios from 'axios';


const location = ref(undefined);
const loadingLocation = ref(false);

async function getDeviceLocation() {

  loadingLocation.value = true;

  navigator.geolocation.getCurrentPosition(position => {
    loadingLocation.value = false;

    location.value = {
      lat: position.coords.latitude,
      long: position.coords.longitude
    };

  }, error => {
    loadingLocation.value = false;
    console.error(error);
  });

}


const locationInfo = ref(undefined);
const loadingInfo = ref(false);
const info = ref('');

watch(location, async () => {
  if (!location.value) return;

  const response = await axios.get('http://localhost:8000/forecast/', { data: location.value });
  const data = response.data;

  info.value = data.properties.timeseries[0].data.instant.details.air_temperature;

});

</script>

<template>
  <v-app>
    <v-main class="bg-grey-lighten-4">
      <v-container class="mx-auto" style="max-width: 768px;">

        <v-card prepend-icon="mdi-earth" title="Get Location" :loading="loadingLocation">

          <v-card-text>
            Please allow getting location to automatically detect location from your device.
          </v-card-text>

          <v-card-actions>
            <v-btn color="primary" @click="getDeviceLocation()">
              Request Location
            </v-btn>
          </v-card-actions>

        </v-card>

        <v-card title="Location Information" class="mt-3">

          <v-card-text v-if="!location">
            No location entered!
          </v-card-text>

          <v-card-text v-if="info">
            Air temprature is {{ info }} celsius.
          </v-card-text>

        </v-card>

      </v-container>
    </v-main>
  </v-app>
</template>
