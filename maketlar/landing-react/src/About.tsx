import { PrimaryButton, SectionBadge } from './ui'
import SMALL from './assets/kurs.webp'
import LARGE from './assets/dashboard.webp'

export default function About() {
  return (
    <section className="overflow-hidden bg-white pb-12 pt-16 sm:pb-16 sm:pt-20 lg:pb-24 lg:pt-32">
      <div className="mx-auto max-w-[1440px]">
        <SectionBadge n={1} label="Platforma bilan tanishing" />

        <h2 className="mb-12 px-5 text-[clamp(1.5rem,4vw,3.2rem)] font-medium leading-[1.12] tracking-[-0.02em] text-[#121A33] sm:mb-16 sm:px-8 lg:mb-28 lg:px-12">
          Tizimli bilim, amaliy natija —
          <br className="hidden sm:block" />
          <span className="sm:hidden"> </span>
          ish joyidan uzilmasdan.
        </h2>

        {/* Mobil / planshet */}
        <div className="px-5 sm:px-8 lg:hidden">
          <p className="text-[15px] font-medium leading-[1.6] text-[#121A33] sm:text-[17px]">
            Onlayn, gibrid va anʼanaviy darslar, elektron jurnal, oʻquv materiallari va QR kodli sertifikat — barchasi bitta tizimda.
          </p>
          <div className="mt-6">
            <PrimaryButton>Loyiha haqida</PrimaryButton>
          </div>
          <div className="mt-10 flex flex-col gap-4 sm:flex-row sm:gap-5">
            <img src={SMALL} alt="Kurs sahifasi" className="aspect-[438/346] w-full rounded-xl object-cover object-left-top sm:w-[45%] sm:rounded-2xl" />
            <img src={LARGE} alt="Tinglovchi kabineti" className="aspect-[900/600] w-full rounded-xl object-cover object-left-top sm:w-[55%] sm:rounded-2xl" />
          </div>
        </div>

        {/* Desktop */}
        <div className="hidden grid-cols-[26%_1fr_48%] items-end gap-6 px-12 lg:grid xl:gap-8">
          <img src={SMALL} alt="Kurs sahifasi" className="aspect-[438/346] w-full self-end rounded-2xl object-cover object-left-top" />
          <div className="flex justify-end self-start">
            <div>
              <p className="whitespace-nowrap text-[16px] font-medium leading-[1.65] text-[#121A33] xl:text-[18px]">
                Onlayn, gibrid va anʼanaviy darslar,
                <br />
                elektron jurnal va QR kodli sertifikat —
                <br />
                barchasi bitta tizimda.
              </p>
              <div className="mt-6">
                <PrimaryButton>Loyiha haqida</PrimaryButton>
              </div>
            </div>
          </div>
          <img src={LARGE} alt="Tinglovchi kabineti" className="aspect-[3/2] w-full self-end rounded-2xl object-cover object-left-top" />
        </div>
      </div>
    </section>
  )
}
