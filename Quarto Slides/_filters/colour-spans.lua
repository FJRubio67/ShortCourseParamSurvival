-- Coloured text spans: [text]{.pop}, [text]{.exc}, [text]{.obs}, [text]{.cens}
-- HTML: coloured by ucl.scss.  PDF (beamer): wrapped in \textcolor with the colours from beamer-ucl.tex.
local colours = { pop = "popcol", exc = "exccol", obs = "obscol", cens = "censcol" }
function Span(el)
  if not quarto.doc.is_format("latex") then return nil end
  for cls, col in pairs(colours) do
    if el.classes:includes(cls) then
      local out = { pandoc.RawInline("latex", "\\textcolor{" .. col .. "}{") }
      for _, x in ipairs(el.content) do table.insert(out, x) end
      table.insert(out, pandoc.RawInline("latex", "}"))
      return out
    end
  end
end
