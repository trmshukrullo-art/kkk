<script setup lang="ts">
import type { Slide } from '~/types'

const props = withDefaults(
  defineProps<{
    slides: Slide[]
    autoplay?: number
  }>(),
  { autoplay: 0 },
)

const current = defineModel<number>({ default: 0 })

const count = computed(() => props.slides.length)

function goTo(index: number) {
  current.value = (index + count.value) % count.value
}

const next = () => goTo(current.value + 1)
const prev = () => goTo(current.value - 1)

let timer: ReturnType<typeof setInterval> | undefined

function stop() {
  clearInterval(timer)
}

function start() {
  stop()
  if (props.autoplay > 0 && count.value > 1) timer = setInterval(next, props.autoplay)
}

onMounted(start)
onBeforeUnmount(stop)
</script>

<template>
  <section
    class="slider"
    aria-roledescription="carousel"
    tabindex="0"
    @keydown.left="prev"
    @keydown.right="next"
    @mouseenter="stop"
    @mouseleave="start"
  >
    <div class="slider__viewport">
      <ul class="slider__track" :style="{ transform: `translateX(-${current * 100}%)` }">
        <li
          v-for="(slide, i) in slides"
          :key="i"
          class="slider__slide"
          :aria-hidden="i !== current"
          :aria-label="`${i + 1} / ${count}`"
        >
          <img v-if="slide.image" :src="slide.image" :alt="slide.title" class="slider__image">
          <div class="slider__content">
            <h3 class="slider__title">{{ slide.title }}</h3>
            <p v-if="slide.text" class="slider__text">{{ slide.text }}</p>
          </div>
        </li>
      </ul>
    </div>

    <div v-if="count > 1" class="slider__controls">
      <button type="button" class="slider__arrow" aria-label="Oldingi slayd" @click="prev">
        &larr;
      </button>

      <div class="slider__dots">
        <button
          v-for="(_, i) in slides"
          :key="i"
          type="button"
          class="slider__dot"
          :class="{ 'slider__dot--active': i === current }"
          :aria-label="`${i + 1}-slaydga o'tish`"
          :aria-current="i === current"
          @click="goTo(i)"
        />
      </div>

      <button type="button" class="slider__arrow" aria-label="Keyingi slayd" @click="next">
        &rarr;
      </button>
    </div>
  </section>
</template>

<style scoped>
.slider {
  outline: none;
}

.slider:focus-visible {
  box-shadow: 0 0 0 3px var(--color-primary-light);
  border-radius: var(--radius-lg);
}

.slider__viewport {
  overflow: hidden;
  border-radius: var(--radius-lg);
  background: var(--color-soft);
}

.slider__track {
  display: flex;
  list-style: none;
  transition: transform 0.5s ease;
}

.slider__slide {
  flex: 0 0 100%;
  min-width: 0;
}

.slider__image {
  display: block;
  width: 100%;
  aspect-ratio: 16 / 7;
  object-fit: cover;
}

.slider__content {
  padding: 32px 40px;
}

.slider__title {
  font-weight: 600;
  font-size: 24px;
  line-height: 32px;
  letter-spacing: -0.3px;
}

.slider__text {
  margin-top: 8px;
  font-size: 16px;
  line-height: 24px;
  color: var(--color-muted);
}

.slider__controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.slider__arrow {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-md);
  border: 1px solid var(--color-border);
  background: var(--color-white);
  color: var(--color-text);
  font-size: 18px;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s;
}

.slider__arrow:hover,
.slider__arrow:focus-visible {
  border-color: var(--color-primary);
  color: var(--color-primary);
}

.slider__dots {
  display: flex;
  gap: 8px;
}

.slider__dot {
  width: 8px;
  height: 8px;
  border: none;
  border-radius: var(--radius-pill);
  background: var(--color-border);
  cursor: pointer;
  transition: width 0.3s, background 0.3s;
}

.slider__dot--active {
  width: 24px;
  background: var(--gradient-primary);
}

@media (max-width: 640px) {
  .slider__content {
    padding: 20px;
  }

  .slider__title {
    font-size: 20px;
    line-height: 28px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .slider__track,
  .slider__dot {
    transition: none;
  }
}
</style>
