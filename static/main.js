var hiddenClass = 'hidden';
var shownClass = 'toggled-from-hidden';

function pokemonSectionHover() {
    var children = this.children;
    for(var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.className === hiddenClass) {
            child.className = shownClass;
        }
    }
}

function pokemonSectionEndHover() {
    var children = this.children;
    for(var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.className === shownClass) {
            child.className = hiddenClass;
        }
    }
}

(function() {
    var pokemonSections = document.getElementsByClassName('pokemonname');
    for(var i = 0; i < pokemonSections.length; i++) {
        pokemonSections[i].addEventListener('mouseover', pokemonSectionHover);
        pokemonSections[i].addEventListener('mouseout', pokemonSectionEndHover);
    }
}());
