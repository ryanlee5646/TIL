<template>
  <div class="py-3">
    <v-layout>

      <v-flex xs8>
        <h2 class="font-weight-regular">{{repos.path_with_namespace}}</h2>
        <p class="subheading mb-1 grey--text text--darken-1 font-weight-light">{{repos.namespace.name}}</p>
      </v-flex>

    </v-layout>
  </div>
</template>

<script>
import GitlabService from '@/services/GitlabService'

export default {
	name: 'Repository',
	props: {
		repos: {type: null}
	},
	data() {
		return {
			stats: {}
		}
	},
  mounted() {
		this.drawStatGraph()
  },
	methods: {
		async drawStatGraph() {
			this.commits = await GitlabService.getCommits(this.repos.id)
		}
	}
}
</script>
