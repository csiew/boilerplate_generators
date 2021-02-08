<template>
  <div class="home">
    <p>
      Pick a framework to start configuring and building a project with it.
    </p>
    <div class="framework-list">
      <FrameworkListItem v-for="framework in frameworks" v-bind:key="framework.id" v-bind:framework="framework" />
    </div>
  </div>
</template>

<script>
import FrameworkListItem from '@/components/FrameworkListItem.vue'

export default {
  name: 'Home',
  components: {
    FrameworkListItem
  },
  data() {
    return {
      frameworks: [
        {
          id: 'express',
          title: 'Express',
          caption: 'Create an Express project. Optionally include nodemon and express-session.'
        },
        {
          id: 'react',
          title: 'React',
          caption: 'Create a React project. Optionally include react-router-dom, material-ui/core, material-ui/icons, and react-markdown.'
        },
        {
          id: 'vue',
          title: 'Vue',
          caption: 'Create a Vue project. Optionally include vue-router and marked.'
        }
      ]
    }
  }
}
</script>

<style scoped>
.framework-list {
  width: 100%;
  margin: 0;
  margin-top: 1rem;
  padding: 0;
  display: inline-flex;
  flex-flow: column;
  align-items: flex-start;
  justify-content: flex-start;
}
</style>
