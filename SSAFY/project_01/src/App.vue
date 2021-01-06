<template>
  <v-app>
    <Headers></Headers>
    <v-content>
      <router-view/>
    </v-content>
    <Footers></Footers>
  </v-app>
</template>

<script>
import store from './store'
import Headers from './components/Headers'
import Footers from './components/Footers'

export default {
	name: 'App',
  components:{
    Headers,
    Footers,
  },
	store,
	data() {
		return {
			//
		}
	}
}
</script>
