main:
	mkdir -p ./ramdisk
	sudo mount -t tmpfs -o size=2046m tmpfs ./ramdisk
	cp *.py *.sh ./ramdisk	
	cd ./ramdisk; python3 csmith_driver.py

clean:
	cd ramdisk; rm -f *.clang *.gcc *.txt test_case_*.c
	cd ramdisk; cp *.c ../Bugs
	sudo umount ./ramdisk
	rm -rf ./ramdisk



