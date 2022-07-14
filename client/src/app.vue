<script setup>

import './assets/styles/app.scss';

import { ref } from '@vue/reactivity';


const location = ref(undefined);
const loadingLocation = ref(false);

async function getDeviceLocation() {

  loadingLocation.value = true;

  navigator.geolocation.getCurrentPosition(position => {
    loadingLocation.value = false;
    console.log(position);
  }, error => {
    loadingLocation.value = false;
    console.error(error);
  });
}

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

      </v-container>
    </v-main>
  </v-app>
</template>
