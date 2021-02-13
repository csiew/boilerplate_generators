<template>
  <div>
    <div class="toolbar justify-space-between">
      <div class="toolbar-group">
        <h2>{{ framework.title }}</h2>
      </div>
      <div class="toolbar-group">
        <button>Next &rarr;</button>
      </div>
    </div>
    <div class="container-scroll container-centered container-m grid padding-l">
      <p>{{ framework.caption }}</p>
      <div class="card">
        <div class="card-header">
          <h3>Project properties</h3>
        </div>
        <div class="card-content">
          <form>
            <input type="text" name="projectName" placeholder="Name" @input="handleNameChange" />
            <input type="text" name="projectAuthor" placeholder="Author" @input="handleAuthorChange" />
          </form>
        </div>
      </div>
      <div v-if="Object.keys(framework).includes('options')" class="card">
        <div class="card-header">
          <h3>Configure options</h3>
        </div>
        <div class="card-content">
          <form>
            <div v-for="[optionKey, optionValue] in Object.entries(framework.options)" v-bind:key="optionKey">
              <input v-bind:name="optionKey" type="checkbox" v-bind:checked="optionValue.value" />
              <label v-bind:for="optionKey">{{ optionValue.title }}</label>
            </div>
          </form>
        </div>
      </div>
      <div class="card">
        <div class="card-header">
          <h3>Additional packages</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FrameworkConfiguration',
  props: {
    framework: Object
  },
  data() {
    return {
      project: {
        name: '',
        author: ''
      }
    }
  },
  methods: {
    handleNameChange() {
      this.name = document.getElementsByName('projectName')[0].value
    },
    handleAuthorChange() {
      this.author = document.getElementsByName('projectAuthor')[0].value
    }
  }
}
</script>
