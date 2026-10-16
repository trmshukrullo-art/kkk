import type { ReactNode } from 'react'
import { ArrowRight } from 'lucide-react'

export const EASE = 'ease-[cubic-bezier(0.25,0.1,0.25,1)]'

/** Hover'da matn yuqoriga aylanadi: matn ikki marta takrorlanadi va -50% siljiydi. */
export function RollText({ children, className = '' }: { children: ReactNode; className?: string }) {
  return (
    <span className={`relative block h-[20px] overflow-hidden ${className}`}>
      <span className={`flex flex-col transition-transform duration-500 ${EASE} group-hover:-translate-y-1/2`}>
        <span className="flex h-[20px] items-center whitespace-nowrap">{children}</span>
        <span className="flex h-[20px] items-center whitespace-nowrap" aria-hidden="true">{children}</span>
      </span>
    </span>
  )
}

/** Asosiy firuza tugma: aylanuvchi matn va -45° buriladigan strelka. */
export function PrimaryButton({ children, href = '#' }: { children: ReactNode; href?: string }) {
  return (
    <a
      href={href}
      className="group inline-flex items-center gap-3 self-start rounded-full bg-[#0D7C78] py-2 pl-5 pr-2 text-[13px] font-medium text-white transition-colors duration-300 hover:bg-[#0A6764] sm:pl-6 sm:text-[14px]"
    >
      <RollText>{children}</RollText>
      <span className="flex h-7 w-7 items-center justify-center rounded-full bg-white sm:h-8 sm:w-8">
        <ArrowRight size={16} className={`text-[#0D7C78] transition-transform duration-500 ${EASE} group-hover:-rotate-45`} />
      </span>
    </a>
  )
}

/** Raqamli badge qatori: lojuvard doira + pill yorliq. */
export function SectionBadge({ n, label, border = 'border-[#E7E0D3]' }: { n: number; label: string; border?: string }) {
  return (
    <div className="mb-6 flex items-center gap-3 px-5 sm:mb-8 sm:px-8 lg:px-12">
      <span className="flex h-6 w-6 items-center justify-center rounded-full bg-[#0F2552] text-[11px] font-semibold text-white sm:h-7 sm:w-7 sm:text-[12px]">
        {n}
      </span>
      <span className={`rounded-full border ${border} px-3 py-1 text-[12px] font-medium text-[#121A33] sm:px-4 sm:py-1.5 sm:text-[13px]`}>
        {label}
      </span>
    </div>
  )
}

/** 8 qirrali girih yulduzi — Axion'dagi yulduz o'rniga. */
export function GirihStar({ className = '' }: { className?: string }) {
  return (
    <svg viewBox="0 0 100 100" className={className} aria-hidden="true">
      <path
        fill="currentColor"
        fillRule="evenodd"
        d="M50 2 L64.1 16.1 L83.9 16.1 L83.9 35.9 L98 50 L83.9 64.1 L83.9 83.9 L64.1 83.9 L50 98 L35.9 83.9 L16.1 83.9 L16.1 64.1 L2 50 L16.1 35.9 L16.1 16.1 L35.9 16.1Z M50 38a12 12 0 1 0 0 24a12 12 0 1 0 0-24Z"
      />
    </svg>
  )
}
