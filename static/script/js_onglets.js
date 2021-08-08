(function(){
    var updawidget = function(links, anime){
        if (anime === undefined){
            anime = true
        }
        var container = links.parentNode.parentNode.parentNode
        var li = links.parentNode
        var present = container.querySelector('.artic.presente')
        var vieuwer = container.querySelector(links.getAttribute('href'))
    
        // verifie si l'element sur lequel on clique son parent a une classe active
        if (li.classList.contains('presente')){
            return false 
        }
        // go to div container
        // selectioner l'anglet qui a l'element actif
        container.querySelector('.mini_nav .presente').classList.remove('presente')
    
        // ajouter la classe presenter sur l'element selectionner
        li.classList.add('presente')
    
        // partie article , on retire l'element presents
        //container.querySelector('.artic.presente').classList.remove('presente')
        // ajouter la classe present
        // pour l'element selectionner , 
        //tout les attribut relative à son href donc adresse leur passe la classe present
        //container.querySelector(links.getAttribute('href')).classList.add('presente')
        
       if (anime){
            // Gestion de transition sur les anglets , code ameliorer
            present.classList.add('fade')
            present.classList.remove('in')
            var fintransition = function (){
                this.classList.remove('fade')
                this.classList.remove('presente')
                vieuwer.classList.add('presente')
                vieuwer.classList.add('fade')
                vieuwer.offsetWidth
                vieuwer.classList.add('in')
                present.removeEventListener('transitionend', fintransition)
                present.removeEventListener('webkitTransitionEnd', fintransition)
                present.removeEventListener('oTransitionEnd', fintransition)

            }
            present.addEventListener('transitionend',fintransition )
            present.addEventListener('webkitTransitionEnd',fintransition )
            present.addEventListener('oTransitionEnd',fintransition )

       } else {
           vieuwer.classList.add('presente')
           vieuwer.classList.remove('presente')
       }
    
    }
    // select all links in class mini_nav
    let all_links = document.querySelectorAll('.mini_nav a')
    // take all links in class with a boucle
    for(var i=0; i < all_links.length; i++){
        // ecouter l'evenements produit :
        all_links[i].addEventListener('click', function(e){
            // lorqu'on lique le lien :
            updawidget(this)
        })
    }
    var haschange = function(e){
        // hash , permet de recuper les ancres de la page
        var h = window.location.hash
        // adresse de la page
        var valeur_adresse = document.querySelector('a[href="' + h + '"]')
        // si l'addresse donner n'existe pas ou si l'element contient deja la classe actif
        if (valeur_adresse !== null && !valeur_adresse.parentNode.classList.contains('presente')){
            updawidget(valeur_adresse, e!== undefined)
        }
    }
    
    window.addEventListener('hashchange', haschange)
    haschange()

})() 