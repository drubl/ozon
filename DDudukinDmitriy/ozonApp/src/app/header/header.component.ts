

import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import {ProductService} from "../services/product.service";
import {UserService} from "../services/user.service";
import {CookieService} from "ngx-cookie-service";

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  @Output() search: EventEmitter<any> = new EventEmitter<any>();
  entranceToLeft:boolean = true;
  public isLogin: string = this.userService.isLogin;
  modalDisplay: boolean = false;
  constructor(private productService: ProductService,
              private userService: UserService) { }
  ngOnInit(): void {
  }
  searchHandler(event: any) {
    this.search.emit(event);
  }
  showModal(){
    this.modalDisplay = !this.modalDisplay;
  }
  registration(){
    this.entranceToLeft = !this.entranceToLeft;
  }
  goBack(){
    this.entranceToLeft = !this.entranceToLeft;
  }
}
