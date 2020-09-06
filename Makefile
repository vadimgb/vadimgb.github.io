all:
	@(echo $(DIVIDER); cd csAndTech; $(MAKE) -k)
	python3 join.py
clean:
	@(echo $(DIVIDER); cd csAndTech; $(MAKE) -k clean)
	rm *.html
