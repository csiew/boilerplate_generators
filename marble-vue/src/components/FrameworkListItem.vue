<template>
  <div class="list-item" v-bind:class="selected ? 'list-item-selected' : ''" @click="handleFrameworkSelection">
    <h2>{{ framework.title }}</h2>
    <sub v-if="framework.caption || framework.caption.length > 0">{{ framework.caption }}</sub>
  </div>
</template>

<script>
export default {
  name: 'FrameworkListItem',
  props: {
    framework: Object,
    selected: Boolean
  },
  methods: {
    handleFrameworkSelection() {
      if (this.framework) {
        try {
          this.$emit('handle-select', this.framework['id'])
        } catch (err) {
          console.warn(err)
        }
      }
    }
  }
}
</script>
