<template>
  <div class="framework-list-item" @click="handleFrameworkSelection">
    <div class="framework-list-item-content">
      <h2>{{ framework.title }}</h2>
      <sub v-if="framework.caption || framework.caption.length > 0">{{ framework.caption }}</sub>
    </div>
    <div class="franework-list-item-arrow">&rarr;</div>
  </div>
</template>

<script>
export default {
  name: 'FrameworkListItem',
  props: {
    framework: Object
  },
  methods: {
    handleFrameworkSelection() {
      if (this.framework) {
        try {
          this.$router.push({ name: 'Create', params: { framework: this.framework } })
        } catch (err) {
          console.warn(err)
        }
      }
    }
  }
}
</script>

<style scoped>
.framework-list-item {
  width: 100%;
  margin: 0;
  padding: 1rem;
  display: inline-flex;
  flex-flow: row;
  align-items: center;
  justify-content: space-between;
  background: whitesmoke;
}
.framework-list-item:nth-child(odd) {
  background: gainsboro;
}
.framework-list-item:hover {
  background: lightgreen;
  cursor: pointer;
}
.framework-list-item:active {
  color: white;
  background: green;
}
.framework-list-item h2 {
  margin: 0;
  margin-bottom: 0.75rem;
}

.framework-list-item-content {
  display: inline-flex;
  flex-flow: column;
  align-items: flex-start;
  justify-content: center;
}

.framework-list-item-arrow {
  font-size: 3rem;
}
</style>
