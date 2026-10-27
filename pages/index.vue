<script setup lang="ts">
import type { Slide } from '~/types'

useSeoMeta({
  title: 'Slider',
  description: 'Oddiy slider namunasi',
})

const slides: Slide[] = [
  {
    title: 'Birinchi slayd',
    text: 'Bu sodda slider namunasi. Strelkalar yoki nuqtalar bilan almashtiring.',
    image: 'https://picsum.photos/id/1018/1200/525',
  },
  {
    title: 'Ikkinchi slayd',
    text: 'Klaviaturadagi ← → tugmalari ham ishlaydi.',
    image: 'https://picsum.photos/id/1015/1200/525',
  },
  {
    title: 'Uchinchi slayd',
    text: 'Sichqoncha ustida turganda avtomatik aylanish to\'xtaydi.',
    image: 'https://picsum.photos/id/1039/1200/525',
  },
]
</script>

<template>
  <main class="page">
    <BaseSlider :slides="slides" :autoplay="4000" />
  </main>
</template>

<style scoped>
.page {
  max-width: 960px;
  margin: 0 auto;
  padding: 48px 16px;
}
</style>
