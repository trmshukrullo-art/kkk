import { useEffect, useState } from 'react'
import { ArrowRight, Clock, Menu, X } from 'lucide-react'
import { Shader, Swirl, ChromaFlow, FlutedGlass, FilmGrain } from 'shaders/react'
import { EASE, GirihStar, PrimaryButton, RollText } from './ui'

const LINKS = ['Kurslar', 'Elektron jurnal', 'Kutubxona', 'Aloqa']

function useTashkentTime() {
  const fmt = () =>
    new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: 'Asia/Tashkent' }).format(new Date())
  const [time, setTime] = useState(fmt)
  useEffect(() => {
    const id = setInterval(() => setTime(fmt()), 1000)
    return () => clearInterval(id)
  }, [])
  return time
}

function Nav({ open, onToggle, time }: { open: boolean; onToggle: () => void; time: string }) {
  return (
    <div className="relative z-20 mx-auto w-full max-w-[1440px] p-2 sm:p-3">
      <nav className="flex items-center justify-between rounded-full bg-white p-[5px]" aria-label="Asosiy menyu">
        <div className="flex items-center gap-6">
          <a href="#" className="flex h-9 w-9 items-center justify-center rounded-full bg-[#0F2552] sm:h-10 sm:w-10" aria-label="Raqamli Malaka — bosh sahifa">
            <span className="text-[10px] font-bold tracking-tight text-white sm:text-[11px]">RM</span>
          </a>
          <div className="hidden items-center gap-6 md:flex">
            {LINKS.map((l) => (
              <a key={l} href="#" className="text-[14px] text-[#121A33] transition-colors duration-300 hover:text-[#5E6577]">
                {l}
              </a>
            ))}
          </div>
        </div>

        <div className="hidden items-center gap-5 md:flex">
          <span className="hidden text-[13px] text-[#5E6577] lg:inline">Kuzgi guruhlarga qabul ochiq</span>
          <span className="flex items-center gap-1.5 text-[13px] text-[#5E6577]">
            <Clock size={14} />
            {time} Toshkentda
          </span>
          <a href="#" className="group flex items-center gap-3 rounded-full bg-[#0F2552] py-2 pl-5 pr-2 text-[13px] font-medium text-white">
            <RollText>Platformaga kirish</RollText>
            <span className="flex h-6 w-6 items-center justify-center rounded-full bg-white">
              <ArrowRight size={14} className={`text-[#0F2552] transition-transform duration-500 ${EASE} group-hover:-rotate-45`} />
            </span>
          </a>
        </div>

        <button
          onClick={onToggle}
          className="flex items-center gap-2 rounded-full bg-[#0F2552] py-2 pl-4 pr-3 text-[13px] font-medium text-white md:hidden"
          aria-expanded={open}
          aria-controls="mobile-menu"
        >
          {open ? 'Yopish' : 'Menyu'}
          {open ? <X size={16} /> : <Menu size={16} />}
        </button>
      </nav>
    </div>
  )
}

function MobileMenu({ open, onClose, time }: { open: boolean; onClose: () => void; time: string }) {
  return (
    <div id="mobile-menu" className={`fixed inset-0 z-50 transition-[visibility] duration-500 md:hidden ${open ? 'visible' : 'pointer-events-none invisible'}`} aria-hidden={!open}>
      <div className={`absolute inset-0 bg-black/60 transition-opacity duration-500 ${open ? 'opacity-100' : 'opacity-0'}`} onClick={onClose} />
      <div
        className={`absolute inset-x-0 bottom-0 mx-3 mb-3 rounded-2xl bg-white p-6 transition-transform duration-500 ease-[cubic-bezier(0.32,0.72,0,1)] ${
          open ? 'translate-y-0' : 'translate-y-full'
        }`}
      >
        <div className="flex items-center justify-between">
          <span className="flex items-center gap-1.5 rounded-full bg-[#F3EDE2] px-3 py-1.5 text-[12px] text-[#5E6577]">
            <Clock size={13} />
            {time} Toshkentda
          </span>
          <button onClick={onClose} className="flex h-9 w-9 items-center justify-center rounded-full bg-[#0F2552] text-white" aria-label="Yopish">
            <X size={16} />
          </button>
        </div>
        <div className="mt-8 flex flex-col gap-2">
          {LINKS.map((l) => (
            <a key={l} href="#" onClick={onClose} className="text-[28px] font-medium leading-tight tracking-[-0.02em] text-[#121A33] sm:text-[32px]">
              {l}
            </a>
          ))}
        </div>
        <a href="#" className="mt-8 flex items-center justify-between rounded-full bg-[#0D7C78] py-2 pl-5 pr-2 text-[14px] font-medium text-white">
          Platformaga kirish
          <span className="flex h-8 w-8 items-center justify-center rounded-full bg-white">
            <ArrowRight size={16} className="text-[#0D7C78]" />
          </span>
        </a>
      </div>
    </div>
  )
}

export default function Hero() {
  const [open, setOpen] = useState(false)
  const time = useTashkentTime()

  return (
    <section className="relative flex min-h-screen flex-col overflow-hidden bg-[#FAF7F1]">
      {/* Statik zaxira fon: GPU bo'lmagan qurilmalarda shader o'rnida ko'rinadi */}
      <div
        className="pointer-events-none absolute inset-0 z-0"
        style={{
          background:
            'radial-gradient(60% 55% at 85% 20%, rgba(22,163,156,0.28), transparent 70%), radial-gradient(45% 45% at 10% 15%, rgba(200,150,62,0.22), transparent 70%), radial-gradient(70% 60% at 60% 110%, rgba(13,124,120,0.18), transparent 70%)',
        }}
      />
      <div className="pointer-events-none absolute inset-0 z-10">
        <Shader className="h-full w-full">
          <Swirl colorA="#ffffff" colorB="#F3EDE2" detail={1.7} />
          <ChromaFlow baseColor="#ffffff" upColor="#16A39C" downColor="#0D7C78" leftColor="#C8963E" rightColor="#16A39C" momentum={13} radius={3.5} />
          <FlutedGlass
            aberration={0.61}
            angle={31}
            frequency={8}
            highlight={0.12}
            highlightSoftness={0}
            lightAngle={-90}
            refraction={4}
            shape="rounded"
            softness={1}
            speed={0.15}
          />
          <FilmGrain strength={0.05} />
        </Shader>
      </div>

      <Nav open={open} onToggle={() => setOpen((v) => !v)} time={time} />
      <MobileMenu open={open} onClose={() => setOpen(false)} time={time} />

      <div className="flex-1" />

      <div className="relative z-20 mx-auto w-full max-w-[1440px] px-5 pb-14 sm:px-8 sm:pb-16 lg:px-12 lg:pb-20">
        <p className="mb-5 text-[13px] tracking-wide text-[#121A33] sm:mb-8 sm:text-[14px]">Raqamli malaka oshirish platformasi</p>
        <h1 className="text-[clamp(1.75rem,7vw,4.2rem)] font-medium leading-[1.08] tracking-[-0.03em] text-[#121A33] sm:text-[clamp(2.5rem,5vw,4.2rem)]">
          Vazirlik xodimlari uchun
          <br className="hidden sm:block" />
          <span className="sm:hidden"> </span>
          malaka oshirishning yagona
          <br className="hidden sm:block" />
          <span className="sm:hidden"> </span>
          <span className="text-[#0D7C78]">raqamli</span> platformasi.
        </h1>

        <div className="mt-8 flex flex-col gap-4 sm:mt-12 sm:flex-row sm:gap-5">
          <PrimaryButton href="#kurslar">Kurslarni koʻrish</PrimaryButton>
          <a
            href="#"
            className="inline-flex items-center gap-2.5 self-start rounded-[4px] bg-white px-3 py-2.5 shadow-[0_2px_8px_rgba(0,0,0,0.08)] transition-shadow duration-300 hover:shadow-[0_4px_16px_rgba(0,0,0,0.12)] sm:py-3"
          >
            <GirihStar className="h-5 w-5 text-[#C8963E] sm:h-6 sm:w-6" />
            <span className="text-[13px] font-medium text-[#121A33] sm:text-[14px]">Rasmiy platforma</span>
            <span className="rounded bg-[#0F2552] px-1.5 py-0.5 text-[10px] text-white sm:px-2 sm:text-[11px]">Vazirlik</span>
          </a>
        </div>
      </div>
    </section>
  )
}
