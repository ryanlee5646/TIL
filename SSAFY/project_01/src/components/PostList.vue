<template>
  <v-layout row wrap mw-700>
    <v-flex v-for="i in posts.length > limits ? limits : posts.length" :class="'xs' + 12 / column" px-3>
      <Post
              :date="posts[i - 1].created_at"
              :title="posts[i - 1].title"
              :body="posts[i - 1].body"></Post>
      <v-divider></v-divider>
    </v-flex>
    <v-flex xs12 text-xs-center round my-5 v-if="loadMore">
      <v-btn color="info" dark v-on:click="loadMorePosts"><v-icon size="25" class="mr-2">fa-plus</v-icon> 더 보기</v-btn>
    </v-flex>
  </v-layout>
</template>
<script>
import Post from '@/components/Post'
import FirebaseService from '@/services/FirebaseService'

export default {
	name: 'PostList',
	props: {
		column: {type: Number, default: 1},
		limits: {type: Number, default: 4},
		loadMore: {type: Boolean, default: false}
	},
	data() {
		return {
			posts: []
		}
	},
	components: {
		Post
	},
	mounted() {
		this.getPosts()
	},
	methods: {
		async getPosts() {
			this.posts = await FirebaseService.getPosts()
		},
		loadMorePosts() {

    }
	}
}
</script>
<style>
  .mw-700 {
    max-width: 700px;
    margin: auto;
  }
</style>
