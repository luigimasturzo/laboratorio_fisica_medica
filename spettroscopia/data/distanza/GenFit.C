//
// Author: E.Gorini (email: edoardo.gorini@le.infn.it)
// Last modification 20/4/2018
// 
// Fits a function with info contained in a text file (i.e. nomefile.txt)
// and plots the graph and the pulls 
// optionally one can not plot the pulls, define a range for fitting and plotting or zoom
// Macro automatically detects if there is a large range in x variable and set log scale in case
//
// First argument is a string variable which contains the name of txt file with information to be plotted
// Second argument is a boolean variable (false,true), which enable or not the plotting of the pulls (default=true)
// Third argument is real variable (default=0) which defines the lower fitting range
// Fourth argument is real variable (default=100) which defines the upper fitting range
// Fifth argument is a boolean variable (false,true), which enable or not the zooming of the plots in the defined range (default=false)
// 
// as usual, the arguments can be omitted when they default to something. 
//
//   example usage:
// Plots and Fit the data contained in nomefile (extension type .txt) and plot also the pulls
//   [0] .x GenFit.C("nomefile"); 
// or, to not plot the pulls
//   [0] .x GenFit.C("nomefile",false); 
// or, to plot the pulls and set the minimum of the x axis range for fitting
//   [0] .x GenFit.C("nomefile",true,0.0)
// or, to not plot the pulls and to set a range (min,max) for fitting
//   [0] .x GenFit.C("nomefile",false,1.0,10.0)
// or, plot the pulls, set a range (1.0,10) for fitting and plot only in the range
//   [0] .x GenFit.C("nomefile",true,1.0,10.0,true)
//
// 
// the txt file should have the following format: 
// info lines should always start with "# " followed by some info
// data lines should be x,y,deltax,deltay 	if the flag is "xyerr"
// data lines should be x,y,deltay 			if the flag is "yerr"
// data lines should be x,y					if the flag is "noerr"
// data points can be removed just adding "# " at the start of the line (line starting with 2.226 is an example)
// data lines are without "# "
// function to be fitted should respect ROOT syntax
// (example of linear fitting,  with initial values 5.1 and 2.2)
/* All the following lines should be put in nomefile.txt
# Titolo del Plot
# Legenda asse x [unita']
# Legenda asse y [unita']
# [0]+[1]*x
# nomeparametro1 nomeparametro2
# 5.1 2.2
# xyerr
4.043	14.000	0.002	0.05
3.573	13.000	0.002	0.05
3.121	12.000	0.003	0.05
2.670	11.000	0.002	0.05
# 2.226	  10.000	0.002	0.05
1.773	9.000	0.002	0.05
1.335	8.000	0.003	0.05
0.927	7.000	0.002	0.05
0.485	6.000	0.003	0.05
*/  
// 
//
//

void GenFit(string file, bool makepulls=true, float min=0, float max=100, bool zoom = false){

// ROOT initialization
  gROOT->Reset();
// graphic   
  gStyle->SetTitleStyle(0);
  gStyle->SetTitleBorderSize(0);
  gStyle->SetTitleX(0.3);
  gStyle->SetTitleY(1.0);
  gStyle->SetTitleH(.1);
  gStyle->SetTitleW(.83);
  if(makepulls)gStyle->SetMarkerSize(0.8);

// print statistics if true, write output file if true 
  bool makestat=true; bool output=true; 
//
  const int maxdec=3;  
//
  if (makestat) {
	gStyle->SetOptStat(1);
	gStyle->SetOptFit(111111);
  }

// here opens the data file, should be a text file, extension .txt (made with WordPad on Windows)
// first check if the extension is txt, if not assumes is a txt file
  if(file.substr(file.length()-4,file.length())!=".txt")file=file+".txt";  

  ifstream in;
  in.open(file.c_str());
// get out if file do not exists.. 
  if(in.is_open()==0){
     in.close();
     gROOT->Reset();
    cout << "File " << file <<" do not exist, exit\n";
    return;
  }
//   
// File exists, start reading the info part
// reads plot title and X and Y labels
  string Title,Xtitle,Ytitle;
  getline(in,Title);  Title=Title.substr(2,Title.length());
  getline(in,Xtitle); Xtitle=Xtitle.substr(2,Xtitle.length());
  getline(in,Ytitle); Ytitle=Ytitle.substr(2,Ytitle.length());
  cout << "\n\tPlot Title is: "<< Title <<"\n";
  cout << "\tx axis title is: "<< Xtitle <<"\n";
  cout << "\ty axis title is: "<< Ytitle <<"\n";

// reads function to fit
  string Function;
  getline(in,Function); Function=Function.substr(2,Function.length());
  cout << "\tFunction to fit is: "<< Function << "\n";
// create the funzione function to be fitted
  TF1 *funzione = new TF1("funzione",Function.c_str(),min,max);
// reads and sets number of parameters of function       
  Int_t numpar=funzione->GetNpar(); 

  cout << "\tNumber of Parameters is: "<< numpar << "\n\twith Initial Values ";

// reads parameter names       
  vector<string> parnames;
  TString buff; 
  in >> buff; 
  if(buff=="#"){
    for (int np=0;np<numpar;np++){
      string sbuf;
      in >> sbuf;
      parnames.push_back(sbuf);
    }
  } else cout << "Parameter names not found exit\n";
  
// read parameter initial values
  TVector pvalue(numpar);
  in >> buff; 
  if(buff=="#"){
    for (int np=0;np<numpar;np++)in >> pvalue(np);
    for (int np=0;np<numpar;np++){
      cout << parnames[np]<< "="<< pvalue[np] << ", ";  
    }
  } else cout << "Parameter initial names not found exit\n";
  cout << "\n";

// reads type of data
  TString flag;
  in >> buff; in >> flag;  
    
// close file
  in.close();


// reopen for data reading
  in.open(file.c_str());  
  TString FileName=file;
  

  cout << "\n\tReading Data, ";    
  TGraphErrors *gr;  
// plot the measurements reading from file 
  if     (flag=="noerr")gr = new TGraphErrors(FileName);
  else if(flag=="xyerr")gr = new TGraphErrors(FileName);
  else if(flag=="yerr" )gr = new TGraphErrors(FileName,"\%lg \%lg \%lg");
  else{
    cout << " wrong flag, exit \n" ;
    return;
  } 
// set plot attributes  
  gr->SetTitle(Title.c_str());
  gr->SetMarkerColor(kBlue);
  gr->SetMarkerStyle(7);
  gr->SetLineColor(kRed);
  gr->GetXaxis()->SetTitle(Xtitle.c_str());
  gr->GetYaxis()->SetTitle(Ytitle.c_str());
// if default limits, set min and max reading range from plot limits  
  if(min==0 & max==100){
  	min=gr->GetXaxis()->GetXmin();
  	max=gr->GetXaxis()->GetXmax();
  	funzione->SetRange(min,max);
  }
  
  const int npo=gr->GetN();
  cout << "found: " <<  npo << " points\n\t------------------------------\n";        

  const int ndec=abs(log10(max-min));
  if(ndec>maxdec)cout << "\tMany decades found, set log x scale\n\t------------------------------\n"; 

// create and set canvas style
  TCanvas *c1 = new TCanvas("c1",Title.c_str(),10,10,900,700);
  c1->SetFillColor(19);
  c1->SetGrid(1,1); 
  if(makepulls)c1->Divide(1,2);
  c1->cd(1);  
  if(ndec>maxdec)gPad->SetLogx();
  
// set parameter names and initial values
  for (int np=0;np<numpar;np++){
    funzione->SetParName(np,parnames[np].c_str());
    funzione->SetParameter(np,pvalue[np]);
  }
// fit in range and plot
  gr->Fit("funzione","QR");
  
// get fit results and print with better precision   
  TF1 *fr=gr->GetFunction("funzione");
  cout << "\tFit Results\n"; 
  for (int np=0;np<numpar;np++){
    cout << "\t" << parnames[np] << " = " << fr->GetParameter(np) << " +/- " << fr->GetParError(np) <<"\n";
  }
  cout << "\n";
  
  // if a zoom then set the limits also in y 
  if(zoom){
    float ymin=fr->Eval(min);
    float ymax=fr->Eval(max); 
    if(ymin>=ymax){
      float ybuf=ymax;
      ymax=ymin;
      ymin=ybuf;
    }   
    gr->GetXaxis()->SetLimits(min,max);
    gr->GetYaxis()->SetRangeUser(0.95*ymin, 1.05*ymax);  
  }
// now plot   
  gr->Draw("AP");
  c1->Update();
  
  if(makepulls){	
// make plot of pulls
	   const int ndof=funzione->GetNDF();	   	   
	   Double_t yy;
       TVectorD pull(npo),xx(npo);

// loop on points
       for (Int_t bin=0;bin<npo;bin++){  
         gr->GetPoint(bin,xx(bin),yy);
// compute the residuals         
         pull(bin) = (yy-funzione->Eval(xx(bin),0.0,0.0));
// Compute now the pulls (normalized residuals) for different cases
// noerror case: the estimated error is sigmaest 
// compute the estimated st.dev. by Fisher method: Chi2/Divided by DOF-1
// R option is important to compute the Chisquare only for used point
         if(flag=="noerr" ){
           pull(bin)=pull(bin)/sqrt(gr->Chisquare(funzione,"R")/(ndof-1));;
         }  
// yerror case: the error is given in the data         
         else if(flag=="yerr" ){
           pull(bin)=pull(bin)/gr->GetErrorY(bin);
         }  
// xyerror case: the error is given in the data but the pulls has to be corrected for the x errors:
// when x errors are present, the error along x is projected along the y-direction by calculating 
// the derivative of the function. it is anyway an approximation 
         else if(flag=="xyerr"){
           pull(bin)=pull(bin)/sqrt( pow((gr->GetErrorY(bin)),2)+pow(fr->Derivative(xx(bin))*gr->GetErrorX(bin),2)); 
         }       
       } 
// now create the Pulls TGraph		
		TGraph *re = new TGraph(xx,pull);

		re->SetTitle(Title.c_str());
		re->SetMarkerColor(kBlue);
		re->SetMarkerStyle(20);
		re->SetMaximum(5);
		re->SetMinimum(-5);
		re->GetXaxis()->SetTitle(Xtitle.c_str());
        re->GetYaxis()->SetTitle("Residui Normalizzati");
        if(zoom)re->GetXaxis()->SetLimits(min,max);
        
        c1->cd(2);
	    c1->SetGrid(1,1);
	    if(ndec>maxdec)gPad->SetLogx();

		re->Draw("AP");
		
// draw a line on plot at zero 
		TLine *tl;
		tl= new TLine(min,0.0,max,0.0);
		tl->SetLineColor(kRed);
		tl->SetLineWidth(3);
		tl->SetLineStyle(2);
		tl->Draw();
		c1->Update();
  }	


// save the plots in pdf with the same name of the original Input File 
  if(output){
  	FileName.Remove(FileName.Length()-4,FileName.Length());
    c1->Print(FileName+".png"); 
  } 
}

