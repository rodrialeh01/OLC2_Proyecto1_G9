import { Component, HostBinding, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { graphviz } from 'd3-graphviz';
import { Archivo } from 'src/app/models/Archivo';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-ast',
  templateUrl: './ast.component.html',
  styleUrls: ['./ast.component.css']
})

export class AstComponent implements OnInit{
  @HostBinding('attr.class') cssClass = 'row';
  archivo : Archivo = {
    texto: ''
  };
  textoG = '';
  constructor(private service: UserService, private router:Router, private activatedRoute: ActivatedRoute) { }
  
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }

  generateAST(){
    this.service.getArbol().subscribe(
      res => {
        this.archivo = res;
        if (this.archivo.texto == ''){
          alert("No se ha generado el arbol de análisis sintáctivco");
          return;
        }
        this.textoG = this.archivo.texto!;
        this.graph();

      },
      err => console.log(err)
    );

  }

  graph(){
    graphviz('#chart').renderDot(this.textoG);
  }
}
