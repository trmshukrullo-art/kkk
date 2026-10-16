import { ArrowRight } from 'lucide-react'
import { SectionBadge } from './ui'

function LinkIcon({ className = '' }: { className?: string }) {
  return (
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className} aria-hidden="true">
      <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" />
      <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" />
    </svg>
  )
}

export default function Courses() {
  return (
    <section id="kurslar" className="bg-[#F3EDE2] pb-16 pt-16 sm:pb-20 sm:pt-20 lg:pb-28 lg:pt-28">
      <div className="mx-auto max-w-[1440px]">
        <SectionBadge n={2} label="Tanlangan kurslar" border="border-[#D9CFBE]" />

        <h2 className="mb-10 px-5 text-[clamp(1.75rem,7vw,4.2rem)] font-medium leading-[1.08] tracking-[-0.03em] text-[#121A33] sm:mb-14 sm:px-8 sm:text-[clamp(2.5rem,5vw,4.2rem)] lg:mb-16 lg:px-12">
          Kurslarimiz
        </h2>

        <div className="grid grid-cols-1 gap-5 px-5 sm:gap-6 sm:px-8 md:grid-cols-2 lg:gap-7 lg:px-12">
          {/* 1-kartochka */}
          <article>
            <a href="#" className="group relative block aspect-[329/246] cursor-pointer overflow-hidden rounded-2xl bg-[#0F2552]">
              <div className="girih absolute inset-0 opacity-[0.12]" />
              <img
                src="./img/dars.webp"
                alt="HR menejment kursidagi dars sahifasi"
                className="absolute inset-x-[7%] top-[9%] w-[86%] rounded-t-xl shadow-[0_20px_50px_-20px_rgba(0,0,0,0.6)] transition-transform duration-700 ease-[cubic-bezier(0.25,0.1,0.25,1)] group-hover:-translate-y-2"
              />
              <span className="absolute bottom-4 left-4 flex h-9 w-9 items-center justify-center overflow-hidden rounded-full bg-white text-[#121A33] transition-all duration-300 ease-in-out group-hover:w-[128px] group-hover:justify-between group-hover:pl-4 group-hover:pr-3">
                <span className="w-0 whitespace-nowrap text-[13px] font-medium opacity-0 transition-opacity delay-100 duration-300 group-hover:w-auto group-hover:opacity-100">
                  Batafsil
                </span>
                <LinkIcon className="shrink-0 -rotate-45 transition-transform duration-300 group-hover:rotate-0" />
              </span>
            </a>
            <p className="mt-4 text-[13px] leading-relaxed text-[#5E6577] sm:text-[14px]">
              5 modul · 72 soat · onlayn — kadrlar siyosatidan strategik HR gacha
            </p>
            <h3 className="mt-1 text-[14px] font-semibold text-[#121A33] sm:text-[15px]">HR menejment</h3>
          </article>

          {/* 2-kartochka */}
          <article>
            <a href="#" className="group relative block aspect-square cursor-pointer overflow-hidden rounded-2xl bg-[#0D7C78]">
              <div className="girih absolute inset-0 opacity-[0.14]" />
              <img
                src="./img/natija.webp"
                alt="Test natijasi sahifasi"
                className="absolute left-[9%] top-[12%] w-[130%] max-w-none rounded-tl-xl shadow-[0_20px_50px_-20px_rgba(0,0,0,0.6)] transition-transform duration-700 ease-[cubic-bezier(0.25,0.1,0.25,1)] group-hover:-translate-y-2"
              />
              <span className="absolute bottom-4 left-4 flex h-9 w-9 items-center justify-center overflow-hidden rounded-full bg-[#0F2552] text-white transition-all duration-300 ease-in-out group-hover:w-[188px] group-hover:justify-between group-hover:pl-4 group-hover:pr-3">
                <span className="w-0 whitespace-nowrap text-[13px] font-medium opacity-0 transition-opacity delay-100 duration-300 group-hover:w-auto group-hover:opacity-100">
                  Kurs dasturini koʻrish
                </span>
                <ArrowRight size={14} className="shrink-0 -rotate-45 transition-transform duration-300 group-hover:rotate-0" />
              </span>
            </a>
            <p className="mt-4 text-[13px] leading-relaxed text-[#5E6577] sm:text-[14px]">
              4 modul · 72 soat · anʼanaviy — ish joyidagi xavflarni baholash va profilaktika
            </p>
            <h3 className="mt-1 text-[14px] font-semibold text-[#121A33] sm:text-[15px]">Mehnatni muhofaza qilish</h3>
          </article>
        </div>
      </div>
    </section>
  )
}
