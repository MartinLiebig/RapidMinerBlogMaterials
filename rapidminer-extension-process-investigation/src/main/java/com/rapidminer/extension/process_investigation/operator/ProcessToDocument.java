package com.rapidminer.extension.process_investigation.operator;

import java.io.File;
import java.io.IOException;
import java.util.List;

import com.rapidminer.Process;
import com.rapidminer.operator.IOObjectCollection;
import com.rapidminer.operator.Operator;
import com.rapidminer.operator.OperatorDescription;
import com.rapidminer.operator.ports.OutputPort;
import com.rapidminer.operator.text.Document;
import com.rapidminer.parameter.ParameterType;
import com.rapidminer.parameter.ParameterTypeDirectory;
import com.rapidminer.parameter.ParameterTypeFile;
import com.rapidminer.parameter.UndefinedParameterError;
import com.rapidminer.tools.OperatorService;
import com.rapidminer.tools.XMLException;


public class ProcessToDocument extends Operator {

	public final static String PARAMETER_DIRECTORY = "directory";

	OutputPort docOut = getOutputPorts().createPort("docs");

	/**
	 * <p>
	 * Creates an unnamed operator. Subclasses must pass the given description object to this super-constructor (i.e.
	 * invoking super(OperatorDescription)). They might also add additional values for process logging.
	 * </p>
	 * <p>
	 * NOTE: the preferred way for operator creation is using one of the factory methods of {@link OperatorService}.
	 * </p>
	 *
	 * @param description
	 */
	public ProcessToDocument(OperatorDescription description) {
		super(description);
	}

	public void doWork() throws UndefinedParameterError {
		//String myDirectoryPath = "C:\\Users\\MartinSchmitz\\.RapidMiner\\repositories\\Local Repository\\Customer Success";
		String myDirectoryPath = getParameterAsString(PARAMETER_DIRECTORY);
		File f = new File(myDirectoryPath);

		IOObjectCollection<Document> outputCollection = new IOObjectCollection<>();
		processFile(f, outputCollection);

		docOut.deliver(outputCollection);

	}

	public void processFile(File dir, IOObjectCollection<Document> output) {
		File[] files = dir.listFiles();
		if (files != null) {
			for (File f : files) {
				if (f.isDirectory()) {
					processFile(f, output);
				} else {
					if (f.toString().endsWith(".rmp")) {
						try {
							Process p = new Process(f);
							StringBuilder sb = new StringBuilder();
							for (Operator o : p.getAllOperators()) {
								sb.append(o.getClass().toString() + "\n");
							}
							output.add(new Document(sb.toString()));
						} catch (IOException e) {
							e.printStackTrace();
						} catch (XMLException e) {
							e.printStackTrace();
						}

					}
				}
			}
		}
	}
	@Override
	public List<ParameterType> getParameterTypes() {
		List<ParameterType> types = super.getParameterTypes();

		types.add(new ParameterTypeDirectory(PARAMETER_DIRECTORY,"Directory of your repository",false));
		return types;
	}
}
