<template>
  <v-layout align-center justify-center row fill-height>
    <v-flex xs5 text-xs-center>
      <v-layout align-center justify-center row fill-height elevation-5 style="min-height:500px;" white pa-4>
        <v-flex xs12 text-xs-center>
          <v-btn round color="#df4a31" dark v-on:click="loginWithGoogle" style="width:100%;"><v-icon size="25" class="mr-2">fa-google</v-icon> Google 로그인</v-btn>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
import FirebaseService from '@/services/FirebaseService'

export default {
	name: 'LoginPage',
	data() {
		return {}
	},
	components: {},
	methods: {
		async loginWithGoogle() {
			const result = await FirebaseService.loginWithGoogle()
			this.$store.state.accessToken = result.credential.accessToken
			this.$store.state.user = result.user
		}
	},
	mounted() {
		console.log(this.$store.state)
	}
}
</script>
