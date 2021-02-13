<template>
  <div class="container container-centered container-m padding-l">
    <div class="card card-list list">
      <div class="toolbar">
        <div class="toolbar-group">
          <h2>Frameworks</h2>
        </div>
      </div>
      <FrameworkListItem v-for="framework in Object.values(frameworks)" v-bind:key="framework.id" v-bind:framework="framework" v-bind:selected="selectedFrameworkId === framework.id ? true : false" @handle-select="handleSelectFramework" />
    </div>
  </div>
</template>

<script>
import FrameworkListItem from '@/components/FrameworkListItem.vue'

export default {
  name: 'FrameworkChooser',
  components: {
    FrameworkListItem
  },
  data() {
    return {
      selectedFrameworkId: '',
      frameworks: {
        'express': {
          id: 'express',
          title: 'Express',
          caption: 'Create an Express project. Optionally include nodemon and express-session.',
          options: {
            'use-nodemon': {
              title: 'Nodemon',
              value: true
            },
            'use-express-session': {
              title: 'Express Session',
              value: false
            }
          }
        },
        'react': {
          id: 'react',
          title: 'React',
          caption: 'Create a React project. Optionally include react-router-dom, material-ui/core, material-ui/icons, and react-markdown.'
        },
        'vue': {
          id: 'vue',
          title: 'Vue',
          caption: 'Create a Vue project. Optionally include vue-router and marked.'
        }
      }
    }
  },
  methods: {
    handleSelectFramework(id) {
      this.$emit('handle-select', id)
    }
  }
}
</script>
