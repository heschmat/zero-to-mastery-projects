# Define variables for image name, container name, and output file
IMAGE_NAME=news_aggregator_script
OUTPUT_DIR=output
OUTPUT_FILE=$(OUTPUT_DIR)/headlines_sample_50.csv

# Default target (runs all necessary steps)
all: build run

# Step 1: Create the output directory if it doesn't exist
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

# Step 2: Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Step 3: Run the Docker container
run: $(OUTPUT_DIR)
	docker run --rm -v "$(PWD)/$(OUTPUT_DIR):/app/output" $(IMAGE_NAME)

# Step 4: Clean up the output directory
clean:
	rm -rf $(OUTPUT_DIR)
