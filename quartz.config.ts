import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Digital Garden di Antonio",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "it-IT",
    baseUrl: "amagaro.github.io/Salvatore_Ricercatore",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "GFS Didot",
        body: {
          name: "Poppins",
          weights: [200, 400],
        },
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#0a0a0f",
          lightgray: "#1e293b",
          gray: "#64748b",
          darkgray: "#e2e8f0",
          dark: "#f8fafc",
          secondary: "#22d3ee",
          tertiary: "#2dd4bf",
          highlight: "rgba(34, 211, 238, 0.15)",
          textHighlight: "#b3aa0288",
        },
        darkMode: {
          light: "#0a0a0f",
          lightgray: "#1e293b",
          gray: "#64748b",
          darkgray: "#e2e8f0",
          dark: "#f8fafc",
          secondary: "#22d3ee",
          tertiary: "#2dd4bf",
          highlight: "rgba(34, 211, 238, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
