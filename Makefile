all: pdf

pdf: overview.pdf
docx: overview.docx

overview.pdf: overview.md 
	pandoc \
		--pdf-engine=C:\Users\HP\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex \
		overview.md -o overview.pdf


overview.docx: overview.md
	pandoc \
		-s \
		overview.md -o overview.docx

.PHONY: clean
clean:
	${RM} overview.pdf overview.docx 