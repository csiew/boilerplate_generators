<template>
  <div>
    <div class="toolbar">
      <button @click="$router.go(-1)">&larr; Back</button>
      <button>Next &rarr;</button>
    </div>
    <h2>{{ framework.title }}</h2>
    <p>{{ framework.caption }}</p>
    <hr />
    <h3>Project properties</h3>
      <form>
        <input type="text" placeholder="Name" />
        <input type="text" placeholder="Author" />
      </form>
    <hr />
    <h3>Configure options</h3>
    <hr />
    <h3>Additional packages</h3>
  </div>
</template>

<script>
export default {
  name: 'Create',
  props: {
    framework: Object
  },
  mounted() {
    console.log(this.props)
  }
}
</script>

<style scoped>
.toolbar {
  width: 100%;
  display: inline-flex;
  flex-flow: row;
  align-items: center;
  justify-content: space-between;
}
</style>
