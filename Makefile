.PHONY: all publish clean 

POSTS_DIR=./posts
OUTPUT_DIR=./output

MD = $(wildcard $(POSTS_DIR)/*.md)
TMP = $(MD:%.md=%_tmp.html)
HTML = $(MD:$(POSTS_DIR)/%.md=$(OUTPUT_DIR)/%.html)

all: $(HTML) $(OUTPUT_DIR)/index.html
	mkdir -p $(OUTPUT_DIR)
	cp ./static/* ./output/

$(POSTS_DIR)/%_tmp.html: $(POSTS_DIR)/%.md
	pandoc $< > $@
	@x=$$(grep -oP '(?<=TIMESTAMP:) *\d+' $@) ;\
	y=$$(date -d "@$$x" +"%a, %b %-d, %Y");\
	$$(sed -i "s/TIMESTAMP: *[0-9]*/$$y/" $@)
	#$$(sed -i "s/TIMESTAMP: *[0-9]*/<span class="timestamp">$$y<\/span>/" $@)

$(OUTPUT_DIR)/index.html: ./templates/index_template.html $(HTML)
	mkdir -p $(OUTPUT_DIR)
	./bin/create_index.py ./templates/index_template.html $(MD) > $@

$(OUTPUT_DIR)/%.html: $(POSTS_DIR)/%_tmp.html ./templates/post_template.html
	mkdir -p $(OUTPUT_DIR)
	./bin/do_include.py ./templates/post_template.html $< -DTITLE="$$(grep -m 1 -oP '(?<=>).*(?=</h1>)' $<)" > $@

publish: all
	./bin/publish.sh

clean:
	rm -rf $(OUTPUT_DIR)
