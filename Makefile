main:
	@mkdir -p ./ramdisk
	@sudo mount -t tmpfs -o size=2046m tmpfs ./ramdisk
	@cp *.py *.sh ./ramdisk	
	@cd ./ramdisk; python3 csmith_driver.py

clean:
	@cd ramdisk; rm -f *.clang *.gcc *.txt test_case_*.c
	@mkdir -p BugsFound
	@find ./ramdisk -name bug*.c -exec cp {} BugsFound/ \; 
	@sudo umount ./ramdisk 2>&1 
	@rm -rf ./ramdisk



