import (
	"maps"
)

func isAnagram(s string, t string) bool {
	
	s_map := make(map[rune]int)

	for _, value := range s {
		s_map[value]++
	}

	t_map := make(map[rune]int)

	for _, value := range t {
		t_map[value]++
	}

	if maps.Equal(s_map, t_map) {
		return true
	}

	return false


}
