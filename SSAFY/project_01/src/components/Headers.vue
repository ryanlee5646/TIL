<template>
  <v-toolbar fixed>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>규진's Blog</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat to='/'>Home</v-btn>
      <v-btn flat to='portfolio'>PortfolioPage</v-btn>
      <v-btn flat to='post'>PostPage</v-btn>
      <v-btn flat to='login'>LoginPage</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
  export default{
    name  : "Headers"
  }
</script>
