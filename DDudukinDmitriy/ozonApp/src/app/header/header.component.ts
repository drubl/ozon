

import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  @Output() search: EventEmitter<any> = new EventEmitter<any>();
  modalDisplay: boolean = false;
  constructor() { }
  ngOnInit(): void {
  }
  searchHandler(event: any) {
    this.search.emit(event);
  }
  showModal(){
    this.modalDisplay = !this.modalDisplay;
  }
}
