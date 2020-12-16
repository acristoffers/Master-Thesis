((LaTeX-mode . ((eval . (setq-local TeX-master (concat (file-name-directory (or load-file-name buffer-file-name)) "document.tex")))
                (eval . (setq-local reftex-default-bibliography (concat (file-name-directory (or load-file-name buffer-file-name)) "bibliothek.bib")))))
 (latex-mode . ((eval . (setq-local TeX-master (concat (file-name-directory (or load-file-name buffer-file-name)) "document.tex")))
                (eval . (setq-local reftex-default-bibliography (concat (file-name-directory (or load-file-name buffer-file-name)) "bibliothek.bib"))))))
