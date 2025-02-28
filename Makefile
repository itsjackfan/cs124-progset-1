CXX = g++
CXXFLAGS = -std=c++17 -Wall -I.  # Include current directory for headers
LDFLAGS = -lm

SOURCES = $(wildcard $(SRCDIR)/*.cpp)
OBJECTS = $(patsubst $(SRCDIR)/%.cpp,$(OBJDIR)/%.o,$(SOURCES))
EXECUTABLE = randmst

# Create directories if they don't exist

all: $(EXECUTABLE)

$(EXECUTABLE): GraphGenerators.o main.o
	$(CXX) $(LDFLAGS) $^ -o $@

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: main.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJDIR)/*.o $(EXECUTABLE)