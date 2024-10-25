# Define man page directory
MANDIR = /usr/local/share/man/man1

.PHONY: install uninstall

# Default installation rule
install:
	@echo "Installing man page..."
	sudo mkdir -p $(MANDIR)
	sudo cp man_page/mvm.1 $(MANDIR)
	sudo gzip -f $(MANDIR)/mvm.1
	sudo chmod 644 $(MANDIR)/mvm.1.gz
	@echo "Man page installed successfully."

# Uninstall rule
uninstall:
	@echo "Uninstalling man page..."
	sudo rm -f $(MANDIR)/mvm.1.gz
	@echo "Man page uninstalled."
